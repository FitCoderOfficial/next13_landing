import React, { Component } from 'react'
import PropTypes from 'prop-types';

class MyComponent extends Component {
  static defaultProps = {
    name : "기본이름"  
  }
  static propTypes = {
    name : PropTypes.string,
    age : PropTypes.number.isRequired 
  }
  
  constructor(props) {
    super(props);
    this.state = {
      number: 0
        }
  }

  render() {
    return (
      <div>
        <p>안녕하세요, 제 이름은 { this.props.name }입니다.</p>
        <p>제 나이는 { this.state.number }살 입니다.</p>
      </div>
    )
  }
}


export default MyComponent;