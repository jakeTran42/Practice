import React, { Component } from 'react';
import logo from '../logo.svg';
import z2 from '../z2icon.ico';
import sharingan from '../tomoe.png';
import Character from '../components/Characters/Character';
import Cockpit from '../components/Cockpit/Cockpit';
import ErrorBoundary from '../components/ErrorHandling/ErrorBoundary';

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

    const renderChar =
          <Character 
          characters={this.state.characters}
          delete={this.deleteCharHandler}
          change={this.nameChangeHandler}
          />

    if (this.state.showChars) {
      showCharacters = (
        <div>
          {renderChar}
        </div>
      );
    }


    return (
    
      <div className={classes.App}>

        <header className={classes.header}>
          <img src={z2} className={classes.logo} alt="logo" />
          <h1 className={classes.title}>Welcome to React</h1>
        </header>

        <p className={classes.intro}>
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>

        <Cockpit
          showChar={this.state.showChars}
          characters={this.state.characters}
          toggle={this.toggleCharHandler}
        />
        
        {showCharacters}
      </div>
      
    );
  }
}

export default App;
