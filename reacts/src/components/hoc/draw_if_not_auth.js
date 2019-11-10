import { connect } from 'react-redux';

const DrawIfNotAuth = props => {
    if(props.myAccount.id === props.id)  return '';
    return props.children;
}

const mapStateToProps = state => ({
    myAccount: state.account,
});

const mapDispatchToProps = {
};
  
export default connect(mapStateToProps, mapDispatchToProps)(DrawIfNotAuth);