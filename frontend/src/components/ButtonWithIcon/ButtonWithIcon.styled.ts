import styled from "styled-components";

export const Button = styled.button`
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 8px;
  padding: 0;
  background-color: transparent;
  border: 0;
  font-family: Nunito Sans;
  font-weight: 600;
  font-size: 14px;
  line-height: 1.36;
  transition: opacity 0.3s ease-in-out;

  &:hover {
    cursor: pointer;
    opacity: 0.55;
  }
`;

export const ButtonIcon = styled.div`
  width: 15px;
  height: 15px;

  svg {
    path {
      fill: #FF8743;
    }
  }
`;

export const Title = styled.span`
  color: #FF8743;
`;
