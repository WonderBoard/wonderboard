import React, {Fragment, useState} from 'react'

const Dashboard = ({setAuth}) => {
    return (
        <div>
            <Fragment>
                <h1>Login</h1>
                <button onClick={() => {setAuth(false)}}>Go to Login</button>
            </Fragment>
        </div>
    )
}

export default Dashboard
