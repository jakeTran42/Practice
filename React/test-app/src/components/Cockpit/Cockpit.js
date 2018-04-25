import React from 'react';
import classes from './Cockpit.css'

const cockpit = (props) => {

    let assignedClasses = [];

    let BtnClass = ''

    if (props.showChar) {
        BtnClass = classes.Red
    }

    if (props.characters.length <= 2) {
      assignedClasses.push(classes.red);
    }
    if (props.characters.length <= 1) {
      assignedClasses.push(classes.bold);
    }

    return (
        <div className={classes.Cockpit} >
            <p className={assignedClasses.join(' ')}>This will turn red!</p>
            <button className={BtnClass} onClick={props.toggle}>Show Character</button>
        </div>
    );
};

export default cockpit;