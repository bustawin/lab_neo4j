from datetime import datetime
from pprint import pprint
from py2neo import Graph

from items import insert_all_query

graph = Graph()


def tests(query: int, test: int):
    if query == 1:
        if test == 1:
            execute_query(query, datetime(2015, 1, 4))
    elif query == 2:
        if test == 1:
            execute_query(query, '1', '1', 'r1')
    elif query == 3:
        if test == 1:  # coge all menos el 3 por MS1
            execute_query(query, 'MS1', datetime(2015, 1, 2), datetime(2015, 1, 1))
    elif query == 4:
        if test == 1:
            execute_query(query, datetime(2015, 1, 1), 'r1')


def drop():
    query = """
        MATCH(n)
        OPTIONAL MATCH (n)-[r]-()
        DELETE n,r
    """
    graph.cypher.execute(query)


def execute_query(query: int, *args):
    # drop everything
    drop()
    result = None
    if query == 1:
        graph.cypher.execute(insert_all_query)
        result = query_1(*args)
    elif query == 2:
        result = query_2(*args)
    elif query == 3:
        graph.cypher.execute(insert_all_query)
        result = query_3(*args)
    elif query == 4:
        graph.cypher.execute(insert_all_query)
        result = query_4(*args)
    pprint(result)


def query_1(date: datetime):
    raise NotImplemented()


def query_2(size: int, part_type: str, region: str) -> list:
    raise NotImplemented()


def query_3(segment: str, date1: datetime, date2: datetime):
    query = """

    """
    result = graph.cypher.execute(query)
    return result


def query_4(date: datetime, region: str):
    date2 = str(date.replace(date.year + 1))
    date = str(date)
    query = """
    MATCH (c: Customer)<-[ORDERED_BY]-(o: Order)-[CONTAINS]->(l:lineItem)->[SUPPLIED_BY]->(s:Supplier)
    WHERE
            o.O_ORDERDATE < """ + date + """ AND
            o.O_ORDERDATE < """ + date2 + """ AND
            c.REGION_NAME = """ + region + """ AND
            s.NATION_NAME = s.NATION_NAME
    RETURN
        s.NATION_NAME as n_name,
        sum((l.L_EXTENDEDPRICE)*(1-l.L_DISCOUNT)) as revenue
    ORDER BY
        revenue DESC
    """
    result = graph.cypher.execute(query)
    return result
