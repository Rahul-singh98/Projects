const express = require('express')
const router = express.Router()
const User = require('../models/User')
const {body, validationResult} = require('express-validator')
const bcrypt = require('bcryptjs')
const jwt = require('jsonwebtoken')

const jwtSecret = "mysupercoolawesomefirstmernapp1234"

router.post('/createuser', [
    body('email', "Please provide a valid mailaddress").isEmail(),
    body('name', "minimum length of name should be 5").isLength({min: 5}),
    body('password', 'minimum length of password should be 5').isLength({min: 5})
], async (req, res) => {
    const errors = validationResult(req);
    if(!errors.isEmpty()) {
        return res.status(400).json({errors:errors.array()});
    }

    // Create a secure password
    const salt = await bcrypt.genSalt();
    const securePass = await bcrypt.hash(req.body.password, salt);

    try {
        await User.create({
            name: req.body.name,
            location: req.body.location,
            email: req.body.email,
            password: securePass
        }).then(res.json({success:true}));
    } catch(err) {
        console.log(err)
        res.json({success:false});
    }
})

router.post('/loginuser', [
    body('email', "Please provide a valid mailaddress").isEmail(),
    body('password', 'minimum length of password should be 5').isLength({min: 5})
], async (req, res) => {
    const errors = validationResult(req);
    if(!errors.isEmpty()) {
        return res.status(400).json({errors:errors.array()});
    }

    const email = req.body.email;

    try {
        const userData = await User.findOne({email});
        if(!userData) {
            return res.status(400).json({errors: "Invalid user credentials"});
        }

        const comparePass = await bcrypt.compare(req.body.password, userData.password)
        if(!comparePass) {
            return res.status(400).json({errors: "Invalid user credentials"});
        }

        const data = { user: { id: userData.id }}
        const authToken = jwt.sign(data, jwtSecret);
        return res.json({ success:true, authToken: authToken });
    } catch(err) {
        console.log(err)
        res.json({success:false});
    }
})

module.exports = router;