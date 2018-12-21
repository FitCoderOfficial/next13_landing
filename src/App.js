import React, { Component } from 'react';
import './App.css';
import MyComponent from './MyComponent';
import EventPractice from './EventPractice';

class App extends Component {
  render() {
    const text = '제가';
    const condition = true;
    const style = {
      backgroundColor: 'grey',
      border: '1px solid black',
      height: Math.round(Math.random() * 300) + 50,
      width: Math.round(Math.random() * 300) + 50,
      WebitTransition:'all',
      MozTransition:'all',
      msTransition:'all'
    }


    return (
      <div className="my-div">
      <MyComponent name="React" age={4}/>
      <h1> 리액트 안녕하세요! </h1>
      <h2> 리액트를 {text} 처음개발했습니다 </h2>
      {
         condition && '보여주세요'
      }
      <div style={style}></div>

      <EventPractice/>
      </div>
    );
  }
}

export default App;
