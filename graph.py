from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)


def initialize_graph():
    with driver.session() as session:

        session.run("MATCH (n) DETACH DELETE n")

        session.run("""
        CREATE (:Product {name: "Laptop", sales_drop: "Yes"})
        CREATE (:Product {name: "Mobile", sales_drop: "No"})
        CREATE (:Region {name: "South"})
        CREATE (:Region {name: "North"})
        CREATE (:Manager {name: "Ravi"})
        CREATE (:Manager {name: "Anita"})
        CREATE (:Category {name: "Electronics"})
        """)

        session.run("""
        MATCH (p:Product {name:"Laptop"}), (r:Region {name:"South"})
        CREATE (p)-[:SOLD_IN]->(r)
        """)

        session.run("""
        MATCH (r:Region {name:"South"}), (m:Manager {name:"Ravi"})
        CREATE (r)-[:MANAGED_BY]->(m)
        """)

        session.run("""
        MATCH (p:Product {name:"Laptop"}), (c:Category {name:"Electronics"})
        CREATE (p)-[:BELONGS_TO]->(c)
        """)


def query_graph():
    with driver.session() as session:
        result = session.run("""
        MATCH (p:Product)-[:SOLD_IN]->(r:Region)
        OPTIONAL MATCH (r)-[:MANAGED_BY]->(m:Manager)
        RETURN p.name AS product,
               r.name AS region,
               m.name AS manager
        """)
        return result.data()