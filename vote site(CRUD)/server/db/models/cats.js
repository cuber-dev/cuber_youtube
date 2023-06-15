
const mongoose = require('mongoose')

const modelName = 'Cats'
const schema = new mongoose.Schema({},{
    strict : false
})
    
const collecName = 'catsCl'
const Cats = new mongoose.model(
    modelName,
    schema,
    collecName
)

module.exports = Cats