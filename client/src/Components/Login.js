import React, {Fragment, useState} from 'react'
import axios from 'axios'

const Login = ({setAuth}) => {
    const [inputs, setInputs] = useState({
        email: "",
        password: "",
    })

    //destruct
const {email, password} = inputs;

const onChange = (e) => {
    // console.log(e.target.value)
    setInputs({...inputs, [e.target.name] : e.target.value})
}

const onSubmitForm = async (e) => {
    e.preventDefault()
    const body = {email, password}
    console.log(body.email)
    try {
        const response = await axios.post('/api/login', body)
        console.log(response.data)

    } catch (err) {
        console.log(err.message)
    }
}
    return (
        <Fragment>
            <h1 style={{marginTop: "50px"}}>Login</h1>
            <form onSubmit={onSubmitForm}>
                <input type="email"
                    name="email"
                    placeholder="email"
                    className="form-control my-3"
                    value={email}
                    onChange={e => onChange(e)}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="password"
                    className="form-control my-3"
                    value={password}
                    onChange={e => onChange(e)}
                />

                <button type="submit" className="btn btn-primary btn-block">Login</button>
            </form>
            {/* <button onClick={() => {setAuth(true)}}>Go to DashBoard</button> */}
        </Fragment>
    )
}

export default Login;
