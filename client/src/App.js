import React, {useState, useEffect} from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import logo from './logo.svg';
import RegisterForm from './Components/register'
import './App.css';
import axios from 'axios';


function App() {
  const [time, timeSet] = useState(0);
  const [email, setEmail] = React.useState("thisEmail");
  const [password, setPassword] = React.useState("e2");

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      timeSet(data.time);
    })
  }, [])

  const handleEmailChange = (inputValue) => {
    setEmail(inputValue);
    
  }


  // const handlPasswordChange = (inputValue) => {
  //   setPassword(inputValue);
  // }

  const handleFormatSubmit = async () => {
    let obj = {hello: "Money"}
    fetch( '/api/register', {
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }, 
    method: 'POST',
    body: {
      'user1':'1234'
    }
  });
    // axios.post('http://127.0.0.1:5000/api/register', obj)
    //         .then(function(response){
    //             console.log(response);
    //    //Perform action based on response
    //     })
    //     .catch(function(error){
    //         console.log(error);
    //    //Perform action based on error
    //     });
    // var json = JSON.stringify(obj);
    // try {
    //   const tru = await axios.post(`/api/register`, json)
    //   console.log(tru.data)
    // } catch (err) {
    //   // Handle error
    // }
  }

  const send = async () => {
    
    try {
      const tru = await axios.post(`/api/register`, {hello: "h"})
      console.log(tru.data)
    } catch (err) {
      // Handle error
    }
  }
    
    return (
    <div className="App">
        <RegisterForm userEmail={email} userPassword={password} onFormChange={handleEmailChange} onFormSubmit={handleFormatSubmit} />
        <p>The time is {time}</p>
        <button onClick={send}>thisBut</button>
        
    </div>
  );
}

export default App;
