# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (t:Tournament {year: $year})<-[:PARTICIPATED_IN]-(team)
RETURN team.name as team
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        year="2019",
        database_="neo4j")
    for record in result.records:
        print(record['team'])
