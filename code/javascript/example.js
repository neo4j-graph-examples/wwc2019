// npm install --save neo4j-driver
// node example.js
const neo4j = require('neo4j-driver');
const driver = neo4j.driver('neo4j://<HOST>:<BOLTPORT>',
                  neo4j.auth.basic('<USERNAME>', '<PASSWORD>'), 
                  {});

const query =
  `
  MATCH (t:Tournament {year: $year})<-[:PARTICIPATED_IN]-(team)
  RETURN team.name as team
  `;

const params = {"year": "2019"};

const session = driver.session({database:"neo4j"});

session.run(query, params)
  .then((result) => {
    result.records.forEach((record) => {
        console.log(record.get('team'));
    });
    session.close();
    driver.close();
  })
  .catch((error) => {
    console.error(error);
  });
