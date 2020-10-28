import React, {Fragment, useState} from 'react';
import axios from 'axios'
const Register = ({setAuth}) => {

    const [inputs, setIntputs] = useState({
        email: "",
        password: "",
        name: ""
    });
    
    const {email, password, username} = inputs;

    const onChange = (e) => {
        setIntputs({...inputs, [e.target.name] : e.target.value})
    }

    const onSubmitForm = async(e) => {
        //tes
        // let testObject = {username: "hae23333222", email: "email@emaild2dd3222223w363.com", password: "daosdk33d", confirmation: "hl3"}
        const body = {email, password, username, confirmation: "hl3"}
        console.log(body)
        e.preventDefault()
        try{
            const response = await axios.post(`/api/register`, body)
            const responseData = response.data
            // console.log(typeof(response.data.success));
            // console.log(response.data)
            if(responseData.success) {
                setAuth(true);
            }
            else {
                alert(responseData.message);
            }
            // success
            console.log(responseData)
        } catch (err) {
            console.log(err.message)
        }
    }



    return ( 
        <Fragment>
             <h1 style={{margin: "100px", textAlign: "center"}}> Register</h1>
            <form onSubmit={onSubmitForm}>
                <input 
                    type="email"
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
                    onChange={e => onChange(e)}
                    value={password}
                />
                <input
                    name="username"
                    placeholder="username"
                    className="form-control my-3"
                    onChange={e => onChange(e)}
                    value={username}
                />
                <button type="submit" className="btn btn-primary btn-block">submit</button>
            </form>
        </Fragment>
    )
}

export default Register
