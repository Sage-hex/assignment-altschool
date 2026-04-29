from pydantic import BaseModel, EmailStr


class BookBase(BaseModel):
    title: str
    author: str
    isbn: str


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    pass


class Member(MemberBase):
    id: int

    class Config:
        from_attributes = True
