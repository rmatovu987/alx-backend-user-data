"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db",
                                     connect_args={"check_same_thread": False})
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds/Saves a new user to the database
        Args:
            email (str): The user's email address
            hashed_password (str): The hashed password of the user
        Returns:
            User: The new user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user given an input
        Args:
            **kwargs: input to search with
        Returns:
            User: The found user or error
        """
        if not kwargs:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound("No user found")
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Updates a user in the database
        Args:
            user_id (int): The user's id
            **kwargs: Input to update the user
        Returns:
            None
        """
        try:
            user = self.find_user_by(id=user_id)
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    raise InvalidRequestError
            self._session.commit()
        except (NoResultFound, InvalidRequestError, ValueError):
            raise ValueError
