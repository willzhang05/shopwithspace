import React from 'react';
import { connect } from 'react-redux';

class StoreResult extends React.Component {
  render() {
    const hover = this.props.marker != null ? 'result hover' : 'result';
    return (
      <div className={hover}>
        <div className='image'></div>
        <div className='text'>
          <h4>{this.props.obj.name}</h4>

          <span className='coords'>
            {this.props.obj.location.lat}, {this.props.obj.location.lng}
          </span>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    marker: state.marker
  };
};

export default connect(mapStateToProps, null)(StoreResult);
