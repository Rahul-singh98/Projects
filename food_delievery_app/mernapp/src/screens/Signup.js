import React, {useState} from 'react'
import { Link } from 'react-router-dom'

export default function Signup() {
    const [credentials, setcredentials] = useState({
        name:"",
        email:"",
        password:"",
        geolocation:""
    })

    const handle_submit = async(e) => {
        e.preventDefault();

        const response = await fetch("http://localhost:5000/api/createuser", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: credentials.name,
                email: credentials.email,
                location: credentials.geolocation,
                password: credentials.password
            })
        })

        const json_response = await response.json()
        console.log(json_response)

        if(!json_response.success) {
            alert("Invalid credentials")
        }
    }

    const onChange = (event) => {
        setcredentials({...credentials, [event.target.name]: event.target.value})
    }

    return (
        <>
        <div className='container'>
            <form onSubmit={handle_submit}>
                <div className="m-3">
                    <label htmlFor="name" className="form-label">Name</label>
                    <input type="text" className="form-control" id="name" name='name' value={credentials.name} onChange={onChange}/>
                </div>
                <div className="m-3">
                    <label htmlFor="email" className="form-label">Email address</label>
                    <input type="email" className="form-control" id="email" aria-describedby="emailHelp" 
                        name='email' value={credentials.email} onChange={onChange}/>
                        <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div className="m-3">
                    <label htmlFor="address" className="form-label">Address</label>
                    <input type="text" className="form-control" id="address" name='geolocation' value={credentials.geolocation} onChange={onChange}/>
                </div>
                <div className="m-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input type="password" className="form-control" id="password" name='password' value={credentials.password} onChange={onChange}/>
                </div>
                
                <button type="submit" className="btn btn-success m-3">Submit</button>
                <Link to="/login" className='btn btn-primary'>Already a user</Link>
            </form>
            </div>
        </>
    )
}
