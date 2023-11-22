from textwrap import dedent


def multiline_text(text: str):
    return dedent(text).replace('\n', ' ').strip().lstrip()


ARTICLE_1 = multiline_text(
    """
    In the most general sense, the Session establishes all conversations with the database and represents a “holding zone”
    for all the objects which you’ve loaded or associated with it during its lifespan.
    It provides the interface where SELECT and other queries are made that will return and modify ORM-mapped objects.
    The ORM objects themselves are maintained inside the Session, inside a structure called the identity map
    - a data structure that maintains unique copies of each object,
    where “unique” means “only one object with a particular primary key”.
    
    The Session begins in a mostly stateless form. Once queries are issued or other objects are persisted with it,
    it requests a connection resource from an Engine that is associated with the Session,
    and then establishes a transaction on that connection.
    This transaction remains in effect until the Session is instructed to commit or roll back the transaction.
    
    The ORM objects maintained by a Session are instrumented such that whenever an attribute or a collection is modified
    in the Python program, a change event is generated which is recorded by the Session.
    Whenever the database is about to be queried, or when the transaction is about to be committed,
    the Session first flushes all pending changes stored in memory to the database.
    This is known as the unit of work pattern.
    
    When using a Session, it’s useful to consider the ORM mapped objects that it maintains
    as proxy objects to database rows, which are local to the transaction being held by the Session.
    In order to maintain the state on the objects as matching what’s actually in the database,
    there are a variety of events that will cause objects to re-access the database in order to keep synchronized.
    It is possible to “detach” objects from a Session, and to continue using them, though this practice
    has its caveats. It’s intended that usually, you’d re-associate detached objects with another Session
    when you want to work with them again, so that they can resume their normal task of representing database state.
    """
)

SUMMARY_1 = (
    'The Session is the interface where queries are made that will '
    'return and modify ORM-mapped objects. The ORM objects themselves '
    'are maintained inside the Session, inside a structure called the '
    'identity map. It is possible to “detach” objects from a Session, '
    'and to continue using them.'
)
