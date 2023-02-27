const express = require('express')
const router = express.Router()

router.post('/foodData', (req, res)=> {
    try {
        res.send([global.food_items, global.food_categories])
    } catch(err) {
        console.error(err)
        res.send({error: "Server Error"})
    }
})

module.exports = router;