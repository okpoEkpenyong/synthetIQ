// const axios = require("axios");

const body = { query: { match_all: {} } };

async function run() {
  const url = "https://v4.aquarius.oceanprotocol.com/api/aquarius/assets/query";
  //   const response = await axios.post(url, body);
  const response = await fetch(url, body);
  console.log("status:", response.status);
  //   console.log(response.data.hits.hits[0]);
  console.log("data:", response.data);
  //   for (const value of response.data.hits.hits) {
  //     console.log(value);
  //   }
}

run();
