const mongoose = require('mongoose');

const mongoURI = "mongodb+srv://rahulrajput98fun:mernapp1234@cluster0.0pojnqf.mongodb.net/foodappmern?retryWrites=true&w=majority"

const mongoDB = async() => {
    await mongoose.connect(mongoURI, { useNewUrlParser: true}, async (err, res)=> {
        if(err) console.log("---", err)
        else {
            console.log("Connected");

            const fetched_data = await mongoose.connection.db.collection('food_items');
            fetched_data.find({}).toArray(function(err, data){
                if(err) console.log("---", err)
                else global.food_items = data
            })

            const food_categories = await mongoose.connection.db.collection('foodCategory');
            food_categories.find({}).toArray(function(err, data){
                if(err) console.log("---", err)
                else global.food_categories = data
            })
        }
    });
}

module.exports = mongoDB