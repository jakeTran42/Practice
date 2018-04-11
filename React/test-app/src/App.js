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
    showChars: false
  }

  nameChangeHandler = (event) => {
    this.setState({
      characters: [
        { name: 'Goro', code: '056' },
        { name: event.target.value, code: '196' },
        { name: 'Futoshi', code: '214' }
      ]
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
      backgroundColor: 'white',
      font: 'inherit',
      border: '2px solid blue',
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
      />)
    })

    if (this.state.showChars) {
      showCharacters = (
        <div>
          {renderChar}
        </div>
      )
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

        <button style={style} onClick={this.toggleCharHandler}>Show Character</button>

        {showCharacters}

      </div>
    );
  }
}

export default App;
