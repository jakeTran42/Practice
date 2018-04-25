import React from 'react';

import Hello from './TestCom/Hello'

const character = (props) => 
    props.characters.map((e, index) => {
        return (
          <Hello
              click={() => props.delete(index)}
              name={e.name}
              code={e.code}
              firstEl={index}
              changeName={(event) => props.change(event, e.id)}
  
          />)
      })


export default character;