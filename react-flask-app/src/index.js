import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Doc1 from './Doc1';
import Doc2 from './Doc2';
import Doc3 from './Doc3';
import Doc4 from './Doc4';
import Doc5 from './Doc5';
import reportWebVitals from './reportWebVitals';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
import { useHistory } from 'react-router'
//const history = useHistory()

ReactDOM.render(
  
    <Router>
      <Route exact path="/">
        <App />
      </Route>
      <Route exact path="/Doc1" >
        <Doc1/>
      </Route>
      <Route exact path="/Doc2">
      <Doc2/>
      </Route>
      <Route exact path="/Doc3">
      <Doc3/>
      </Route>
      <Route exact path="/Doc4">
      <Doc4/>
      </Route>
      <Route exact path="/Doc5">
      <Doc5/>
      </Route>
    </Router>,
  document.getElementById('root')
);
function printwkwk(){
  console.log("wkwk")
}
//location.reload();
// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
