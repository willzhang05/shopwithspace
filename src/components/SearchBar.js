import React from 'react';
import { connect } from 'react-redux';

class SearchBar extends React.Component {
  render() {
    return <div>search bar</div>;
  }
}

const mapStateToProps = state => {
  return {
    result: state.result
  };
};

export default connect(mapStateToProps, null)(SearchBar);
