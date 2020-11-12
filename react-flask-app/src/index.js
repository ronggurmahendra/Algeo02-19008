import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Doc1 from './Doc1';
import reportWebVitals from './reportWebVitals';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
ReactDOM.render(
    <Router>
      <Route exact path="/">
        <App />
      </Route>
      <Route exact path="/Doc1">
        <Doc1/>
      </Route>
      <Route path="/Doc2">
      <Doc1/>
      </Route>
      <Route path="/Doc3">
      <Doc1/>
      </Route>
      <Route path="/Doc4">
      <Doc1/>
      </Route>
      <Route path="/Doc5">
      <Doc1/>
      </Route>
    </Router>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
