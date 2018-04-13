import React from 'react';
import classes from './Hello.css'

const hello = (props) => {
  return (
    <div className={classes.Character}>
      {
        props.firstEl === 0 ? <h2 onClick={props.click}>This is a functional Component</h2> : null
      }
      <h2>This prop character is: [{props.name}] Code: [{props.code}]</h2>
      <input type='text' onChange={props.changeName} value={props.name} />
    </div>
  )
}

export default hello;
