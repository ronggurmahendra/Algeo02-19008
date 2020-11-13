import React, { useState, useEffect, Component } from 'react';
import './App.css';
//import { Form, Input, Rating, Button } from "semantic-ui-react";

import ReactDOM from 'react-dom';
//import { Router, Route, Link, browserHistory, IndexRoute } from 'react-router'

import axios from 'axios';
//import Contact from './Dokumen';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect
} from "react-router-dom";
/*
export class  Doc1 extends React.Component{
    constructor(props){
        super(props);
        //console.log(this.props);
        this.props = props;
        let result = 0;
        //console.log("props",props)
        //const [currentResult, setCurrentResult] = useState(0);
        
        console.log("masuk sini")
        fetch('/result').then(res => res.json()).then(data => {
          console.log("result received")
          //setCurrentResult(data.content);
          result = data.content;
          //console.log(result);
          //console.log(data.content)
        });
    }

    render(){

        console.log(this.props)
        return(
            <div className="Doc1">
                <p>Test{this.props.children.result[0].body}</p>
                <p>{this.props.children.result[0].title}</p>
            </div>
            )
        }
    
}
*/

function Doc5(props) {
    const [currentResult, setCurrentResult] = useState(0);
    useEffect(() => {
        //console.log("masuk sini")
        fetch('/result').then(res => res.json()).then(data => {
            if(data){
                console.log("result received")
                console.log("data",data)
              setCurrentResult(data.content);
              console.log(currentResult);
            }
        });
      }, []);
      console.log(currentResult)
    if (currentResult == 0){
        return(
            <div className="Doc1">
                <p>masukin doc1</p>
            </div>
        )
    }else{
        return (
            <div>
            <p>{currentResult[4].title}</p>
            <p>{currentResult[4].body}</p>
            </div>
            )
    }
}

export default Doc5;