# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "neo4j://<HOST>:<BOLTPORT>",
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (t:Tournament {year: $year})<-[:PARTICIPATED_IN]-(team)
RETURN team.name as team
'''

with driver.session(database="neo4j") as session:
  results = session.read_transaction(
    lambda tx: tx.run(cypher_query,
                      year="2019").data())
  for record in results:
    print(record['team'])

driver.close()
