
const Cats = require('../models/cats')

const updateOne = async (query) => {
    try {
        const result = await Cats.updateOne(query.filter,query.update)
        return { message : "updateOne action successful"}
    } catch (error) {
        console.log(error)
    }
}

const read = async () => {
    try {
        const result = await Cats.find()
        return { result, message : "read action successful"}
    } catch (error) {
        console.log(error)
    }
}
 

module.exports = {
    updateOne,
    read
} 