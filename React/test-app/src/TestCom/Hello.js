import React from 'react';
import './Hello.css'
import Radium from 'radium';

const hello = (props) => {

  const style = {
    backgroundColor: '#222',
    color: 'white',
    '@media (min-width: 500px)': {
      width: '450px'
    }
  };

  return (
    <div className='Character' style={style}>
      <h2 onClick={props.click}>This is a functional Component</h2>
      <h2>This prop character is: [{props.name}] Code: [{props.code}]</h2>
      <input type='text' onChange={props.changeName} value={props.name} />
    </div>
  )
}

export default Radium(hello);
