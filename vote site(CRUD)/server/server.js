// require's
const cors = require('cors')
const express = require('express')
const { connectDB } = require('./db/db-connect')
const { getVotes } = require('./s-controllers/s-controller')

// intialization's
const app = express()
const port = process.env.PORT || 3000


// middlewares
app.use(express.urlencoded({ extended : false}))
app.use(express.json())
app.use(cors({
    origin : '*',
    credentials : true
}))



app.post('/api/v1/voters',async (req,res) => {
    const { cat } = req.body
    console.log(cat)
    if(!cat){
        res.status(404).json({
            accepted : false,
            cat,
            message : 'please send the cat value'
        })
        return;
    }
  
    try {
            const response = await connectDB({ 
                first : { 
                    query : {
                        filter : { name : cat },
                        update : { $inc : { votes : 1 } }
                    },
                    action : 'update-one'
                },
                second : {
                    query : {
                        filter : { totalCatVotes : { $exists : true } },
                        update : { $inc : { totalCatVotes : 1 } } 
                    }, 
                    action : 'update-one'
                },
                third : {
                    action : 'read'  
                }
            })
            const votes = getVotes(response)
                
            res.json({  
                accepted : true,
                cat,
                votes,
                message : response.message
            })
    } catch (error) {
        console.log(error)
        res.status(500).json({
            accepted : true,
            message : 'Internal Server Error (500), Failed to do read-write operations'
        })
    }
})

app.get('*',(req,res) => {
    res.status(404).end('404 Not Found')
})

app.listen(port,() => {
    console.log(`Server is running on port ${port}`)
})

