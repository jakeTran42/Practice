import React from 'react';
import './Hello.css'

const contentStyle = {
  backgroundColor: '#222',
  color: 'white'
}

const hello = (props) => {
  return (
    <div style={contentStyle} className='Character'>
      <h2 onClick={props.click}>This is a functional Component</h2>
      <h2>This prop character is: [{props.name}] Code: [{props.code}]</h2>
      <input type='text' onChange={props.changeName} value={props.name} />
    </div>
  )
}

export default hello;
