import styled from "styled-components";

export const Button = styled.button`
  padding: 6px 10px;
  background-color: transparent;
  border-radius: 4px;
  border: 1px solid #56FF9ED9;
  color: #56FF9EBF;
  font-family: Actay Wide;
  font-weight: 700;
  font-size: 12px;
  line-height: 1.25;
  transition: opacity 0.3s ease-in-out;

  &:hover {
    cursor: pointer;
    opacity: 0.7;
  }
`;
