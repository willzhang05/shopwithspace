import React from 'react';
import { connect } from 'react-redux';

class SearchBar extends React.Component {
  render() {
    return (
      <div className='search-bar-container'>
        <input
          type='text'
          placeholder='Search for items in nearby stores..'
          className='search-bar'
        />
        <button id='search-bar-submit'>
          <i className='fas fa-search'></i>
        </button>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    result: state.result
  };
};

export default connect(mapStateToProps, null)(SearchBar);
