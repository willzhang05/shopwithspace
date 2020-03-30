import React from 'react';
import { connect } from 'react-redux';
import { updateTerm, searchStores } from './SearchBarActions';

class SearchBar extends React.Component {
  searchStores() {
    this.props.searchStores();
  }
  render() {
    return (
      <div className='search-bar-container'>
        <input
          type='text'
          placeholder='Search for item in nearby stores..'
          className='search-bar'
          value={this.props.searchTerm}
          onChange={e => this.props.updateTerm(e.target.value)}
        />
        <button id='search-bar-submit' onClick={this.searchStores.bind(this)}>
          <i className='fas fa-search'></i>
        </button>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    result: state.result,
    searchTerm: state.searchTerm
  };
};

const mapDispatchToProps = {
  updateTerm,
  searchStores
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchBar);
