import React, { Component } from 'react';
import './App.css';
import MyComponent from './MyComponent';

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
      <MyComponent/>
      <h1> 리액트 안녕하세요! </h1>
      <h2> 리액트를 {text} 처음개발했습니다 </h2>
      {
         condition && '보여주세요'
         
      }
      <div style={style}
      // 셀프 클로즈 태그에서만 작동하는 주석
      // 마지막 />가 꼭 새 줄에 있어야 합니다.
      /* 이렇게 작성할 수 있습니다 */
      />
      //이렇게 쓰는 것은 렌더링됩니다
      /* 여기에서는 주석을 못써요 */
      </div>
    );
  }
}

export default App;
