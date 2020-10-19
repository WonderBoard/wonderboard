import React from 'react'



const RegisterForm = (props) => {
    
    const emailChange = (event) => {
        props.onFormChange(event.target.value)
    }

    const handleFormSubmit = (event) => {
        event.preventDefault()
        props.onFormSubmit()
    }
    return (
        <div>
            <form onSubmit={props.handleFormSubmit}>
                <div style={{display: "flex", flexDirection: "column", margin: "auto"}}>
                    <label> Email: 
                    <input type="text" style={{width: 300}} size="50" value={props.userEmail} onChange={emailChange}/>
                    </label>
                    <input type='submit'></input>
                    {/* <label> Password: 
                    <input type="text" style={{width: 300}} size="50" onChange={passwordChange} value={props.userPassword}/>
                    </label> */}
                </div>
            </form>
        </div>
    )
}

export default RegisterForm;
