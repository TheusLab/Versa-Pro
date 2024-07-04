// frontend/reducers/editorReducer.ts
import { handleActions } from 'redux-actions';

const initialState = {
  editorState: {}
};

const editorReducer = handleActions({
  SET_EDITOR_STATE: (state, action) => ({ ...state, editorState: action.payload })
}, initialState);

export default editorReducer;
