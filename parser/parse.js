const xmlParse = require('xml2js').parseString;
const fs = require('fs');
const path = require('path');
const util = require('util');

const readFile = util.promisify(fs.readFile);
const writeFile = util.promisify(fs.writeFile);
const parseString = util.promisify(xmlParse);

const files = [
  'reut2-000.xml',
  'reut2-001.xml',
  'reut2-002.xml',
  'reut2-003.xml',
  'reut2-004.xml',
  'reut2-005.xml',
  'reut2-006.xml',
  'reut2-007.xml',
  'reut2-008.xml',
  'reut2-009.xml',
  'reut2-010.xml',
  'reut2-011.xml',
  'reut2-012.xml',
  'reut2-013.xml',
  'reut2-014.xml',
  'reut2-015.xml',
  'reut2-016.xml',
  'reut2-017.xml',
  'reut2-018.xml',
  'reut2-019.xml',
  'reut2-020.xml',
  'reut2-021.xml',
];

extractAll(files);

async function extractAll(files) {
    for (let f = 0; f < files.length; f++) {
        let json = await extract(files[f]);
        const jsonFilename = files[f].replace('.xml', '.json');
        await writeFile(path.resolve(__dirname, '..', 'data', jsonFilename), JSON.stringify(json))
    }
}

async function extract(filename) {
    let xmlString = await readFile(path.resolve(__dirname, '..', 'data', filename));
    let xml = await parseString(xmlString);
    let articles = xml.MAIN.REUTERS;
    let json = [];
    for (let a = 0; a < articles.length; a++) {
        let article = articles[a];
        if (getBody(article) && getTopic(article)) {
          let testing = getTesting(article);
          let body = getBody(article);
          let topic = getTopic(article);
          json.push({body, topic, testing})
        }
    }

    return json;
}

function getBody(val) {
    if (val && val.TEXT && val.TEXT[0] && val.TEXT[0].BODY && val.TEXT[0].BODY[0]) {
        return val.TEXT[0].BODY[0];
    } else {
        return false;
    }
}

function getTopic(val) {
  if (val && val.TOPICS && val.TOPICS[0] && val.TOPICS[0].D && val.TOPICS[0].D[0] ) {
    return val.TOPICS[0].D[0];
  } else {
    return false;
  }
}

function getTesting(val) {
  if (val && val.$ && val.$.LEWISSPLIT && val.$.LEWISSPLIT === 'TEST' ) {
    return true;
  } else {
    return false;
  }
}