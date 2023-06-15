require('dotenv').config()

const mongoose = require('mongoose')
const controller = require('./controllers/controller')
const db = {  collection : controller }
 
 
async function doOperation(data){
    try {
        const { action , query } = data
        switch(action){
            case 'update-one':
                await db.collection.updateOne(query)
                console.log('updated one')
                break
            case 'read':
                console.log('read')
                return await db.collection.read()
            default :
                return { message : "Invalid Action"}
        }
    } catch (error) {
        console.log(error)
        return { message : `Internal Server Error , failed to do ${action} action`}
    }
}

async function connectDB(data){
    try {
        const status = await mongoose.connect(process.env.DATABASE_URI, {
            useNewUrlParser: true,
        }) 
        if(status){
            console.log('------------------------------')
            console.log('connected to database!')
            await doOperation(data.first)
            await doOperation(data.second)
            return await doOperation(data.third)
        } 
    } catch (error) { 
        console.log('failed to connect to database')
        return "Internal Server , Failed to connnect-to-db (500)"
    }finally{
        mongoose.disconnect()
        console.log('disconnected from database')
        console.log('------------------------------')
    }
}

module.exports = { connectDB }