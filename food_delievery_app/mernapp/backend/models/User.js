const mongoose = require('mongoose')
const { Schema } = mongoose

const UserSchema = new Schema({
    name: {
        type: String,
        required: true
    },
    location: {
        type: String,
        requried: true
    },
    email: {
        type: String,
        requried: true
    },
    password: {
        type: String,
        requried: true
    },
    date: {
        type: Date,
        default: Date.now
    }
})

module.exports = mongoose.model('user', UserSchema)