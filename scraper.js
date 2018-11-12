const path = require('path')
const {launch} = require('rwv-sqlite')
const getDB = require('rwv-sqlite/lib/db')
const InsertStream = require('rwv-sqlite/lib/stream')

let insert
let source
let dbHandle


const go = async () => getDB( path.resolve('./config/database.json'), false )
  .then( ({DB, migrations}) => {
    insert = new InsertStream({}, DB)
    return launch( insert, 'bash', ['./runner.sh'] )
  })

go()
