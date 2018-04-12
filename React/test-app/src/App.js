import React, { Component } from 'react';
import logo from './logo.svg';
import z2 from './z2icon.ico';
import sharingan from './tomoe.png';
import Hello from './TestCom/Hello';
import ErrorBoundary from './ErrorHandling/ErrorBoundary';

import classes from'./App.css';

class App extends Component {

  state = {
    characters: [
      { id: 1, name: 'Zero Two' || 'Goro', code: '002' },
      { id: 2, name: 'Hiro', code: '016' },
      { id: 3, name: 'Ichigo', code: '015' }
    ],
    showChars: true
  }

  nameChangeHandler = (event, id) => {

    const personIndex = this.state.characters.findIndex(char => {
      return char.id === id;
    })

    const person = {...this.state.characters[personIndex]}
    person.name =  event.target.value

    const persons = [...this.state.characters]
    persons[personIndex] = person

    this.setState({
      characters: persons
    })
  }

  toggleCharHandler = () => {
    const doesShow = this.state.showChars;
    this.setState(
      {
        showChars: !doesShow
      }
    );
  }

  deleteCharHandler = (charIndex) => {
    const theseCharacters = this.state.characters.slice();
    theseCharacters.splice(charIndex, 1);
    this.setState({characters: theseCharacters})
  }

  render() {

    {/* This is Inline Style */}

    let showCharacters = null
    let BtnClass = '';

    const renderChar = this.state.characters.map((e, index) => {
      return (
        <ErrorBoundary key={e.id}>
        <Hello
            click={() => this.deleteCharHandler(index)}
            name={e.name}
            code={e.code}
            firstEl={index}
            changeName={(event) => this.nameChangeHandler(event, e.id)}

        />
      </ErrorBoundary>)
    })

    if (this.state.showChars) {
      showCharacters = (
        <div>
          {renderChar}
        </div>
      );
      
      BtnClass = classes.Red
    }

    let assignedClasses = [];

    if (this.state.characters.length <= 2) {
      assignedClasses.push(classes.red);
    }
    if (this.state.characters.length <= 1) {
      assignedClasses.push(classes.bold);
    }

    return (
    
      <div className={classes.App}>

        <header className={classes.header}>
          <img src={sharingan} className={classes.logo} alt="logo" />
          <h1 className={classes.title}>Welcome to React</h1>
        </header>

        <p className={classes.intro}>
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>

        <p className={assignedClasses.join(' ')}>This will turn red!</p>

        <button className={BtnClass} onClick={this.toggleCharHandler}>Show Character</button>

        {showCharacters}

      </div>
      
    );
  }
}

export default App;
