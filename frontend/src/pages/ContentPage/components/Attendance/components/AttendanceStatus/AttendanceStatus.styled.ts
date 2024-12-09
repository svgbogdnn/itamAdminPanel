import styled from "styled-components";
import IconEdit from '@src/assets/images/icon-edit.svg?react';

export const Container = styled.div`
  align-self: center;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 21px;
  width: 100%;
`;

export const EditIcon= styled(IconEdit)`
  transition: opacity 0.3s ease-in-out;

  path {
    fill: #E9EAECBF;
  }

  &:hover {
    cursor: pointer;
    opacity: 0.7;
  }
`;
