import React, { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom';

export default function Login() {
  const [credentials, setcredentials] = useState({
    email: "",
    password: "",
  })
  let navigate = useNavigate()

  const handle_submit = async (e) => {
    e.preventDefault();

    const response = await fetch("http://localhost:5000/api/loginuser", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: credentials.email,
        password: credentials.password
      })
    })

    const json_response = await response.json()
    console.log(json_response)

    if (!json_response.success) {
      alert("Invalid credentials")
    }
    
    if(json_response.success) {
      localStorage.setItem("authToken", json_response.authToken)
      navigate('/')
    }
  }

  const onChange = (event) => {
    setcredentials({ ...credentials, [event.target.name]: event.target.value })
  }

  return (
    <>
        <div className='container'>
            <form onSubmit={handle_submit}>
                <div className="m-3">
                    <label htmlFor="email" className="form-label">Email address</label>
                    <input type="email" className="form-control" id="email" aria-describedby="emailHelp" 
                        name='email' value={credentials.email} onChange={onChange}/>
                        <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div className="m-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input type="password" className="form-control" id="password" name='password' value={credentials.password} onChange={onChange}/>
                </div>
                
                <button type="submit" className="btn btn-success m-3">Submit</button>
                <Link to="/createuser" className='btn btn-primary'>New User</Link>
            </form>
            </div>
        </>
  )
}
