
const filter = (data) => {
    const filtered = {
        totalCatVotes : data[0].totalCatVotes,
        cat1 : data[1].votes,
        cat2 : data[2].votes,
        cat3 : data[3].votes,
        cat4 : data[4].votes,
    }
    return filtered 
}
const getVotes = (data) => { 
    const { result } = data
    const filtered = filter(result)
    const votes = {
        cat1 : {
            percent : `${((filtered.cat1 / filtered.totalCatVotes) * 100).toFixed(2)}%`
        },
        cat2 : {
            percent : `${((filtered.cat2 / filtered.totalCatVotes) * 100).toFixed(2)}%`
        },
        cat3 : {
            percent : `${((filtered.cat3 / filtered.totalCatVotes) * 100).toFixed(2)}%`
        },
        cat4 : {
            percent : `${((filtered.cat4 / filtered.totalCatVotes) * 100).toFixed(2)}%`
        },
    }
    
    return votes
}


module.exports = {
    getVotes
}