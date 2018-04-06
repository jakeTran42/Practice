import React from 'react';

const hello = (props) => {
  return (
    <div>
      <h2 onClick={props.click}>This is a functional Component</h2>
      <h2>This prop character is: [{props.name}] Code: [{props.code}]</h2>
    </div>
  )
}

export default hello;
