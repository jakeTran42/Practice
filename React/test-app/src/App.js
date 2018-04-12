import React, { Component } from 'react';
import logo from './logo.svg';
import z2 from './z2icon.ico';
import sharingan from './tomoe.png';
import Hello from './TestCom/Hello';
import './App.css';

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
    const style = {
      backgroundColor: 'green',
      font: 'inherit',
      border: '1px solid blue',
      padding: '8px',
      cursor: 'pointer'
    }

    let showCharacters = null

    const renderChar = this.state.characters.map((e, index) => {
      return (
      <Hello
          click={() => this.deleteCharHandler(index)}
          name={e.name}
          code={e.code}
          key={e.id}
          changeName={(event) => this.nameChangeHandler(event, e.id)}

      />)
    })

    if (this.state.showChars) {
      showCharacters = (
        <div>
          {renderChar}
        </div>
      )
      style.backgroundColor = 'red'
    }

    let classes = [];

    if (this.state.characters.length <= 2) {
      classes.push('red');
    }
    if (this.state.characters.length <= 1) {
      classes.push('bold');
    }

    return (
      <div className="App">

        <header className="App-header">
          <img src={sharingan} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>

        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>

        <p className={classes.join(' ')}>This will turn red!</p>

        <button style={style} onClick={this.toggleCharHandler}>Show Character</button>

        {showCharacters}

      </div>
    );
  }
}

export default App;
