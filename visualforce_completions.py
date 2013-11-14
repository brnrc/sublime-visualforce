import sublime, sublime_plugin
import re

# Provide completions that match just after typing an opening angle bracket
# based on html_completions.py and visualforce completions by 
# github.com/jairzh/sublime-sfdc-assist/blob/master/visualforce_completions.py
class VisualforceCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0],
                "text.html.visualforce"):
            return []

        pt = locations[0] - len(prefix) - 1
        ch = view.substr(sublime.Region(pt, pt + 1))
        if ch != '<':
            return []

        return ([
            ("apex:actionFunction\tVF", "apex:actionFunction name=\"$1\" action=\"$2\" rerender=\"$3\" status=\"$4\"/>"),
            ("apex:actionPoller\tVF", "apex:actionPoller action=\"$1\" rerender=\"$2\" interval=\"$3\"/>"),
            ("apex:actionRegion\tVF", "apex:actionRegion>\n\t$1\n</apex:actionRegion>"),
            ("apex:actionStatus\tVF", "apex:actionStatus id=\"$1\"/>"),
            ("apex:actionSupport\tVF", "apex:actionSupport event=\"$1\" action=\"$2\" rerender=\"$3\" status=\"$4\"/>"),
            ("apex:attribute\tVF", "apex:attribute name=\"$1\" description=\"$2\" type=\"$3\" required=\"${4:true}\"/>"),
            ("apex:column\tVF", "apex:column value=\"$1\"/>"),
            ("apex:commandButton\tVF", "apex:commandButton action=\"$1\" value=\"$2\" id=\"$3\"/>"),
            ("apex:commandLink\tVF", "apex:commandLink action=\"$1\" value=\"$2\" id=\"$3\"/>"),
            ("apex:component\tVF", "apex:component>\n\t$1\n</apex:component>"),
            ("apex:componentBody\tVF", "apex:componentBody />"),
            ("apex:composition\tVF", "apex:composition template=\"$1\">\n\t$2\n</apex:composition>"),
            ("apex:dataList\tVF", "apex:dataList value=\"$1\" var=\"$2\" id=\"$3\">\n\t$4\n</apex:dataList>"),
            ("apex:dataTable\tVF", "apex:dataTable value=\"$1\" var=\"$2\" id=\"$3\">\n\t$4\n</apex:dataTable>"),
            ("apex:define\tVF", "apex:define name=\"$1\"/>"),
            ("apex:detail\tVF", "apex:detail subject=\"$1\" relatedList=\"${2:false}\" title=\"${3:false}\"/>"),
            ("apex:dynamicComponent\tVF", "apex:dynamicComponent componentValue=\"$1\"/>"),
            ("apex:emailPublisher\tVF", "apex:emailPublisher />"),
            ("apex:enhancedList\tVF", "apex:enhancedList type=\"$1\" height=\"$2\" rowsPerPage=\"$3\" id=\"$4\"/>"),
            ("apex:facet\tVF", "apex:facet name=\"$1\">$2<apex:facet/>"),
            ("apex:flash\tVF", "apex:flash src=\"$1\" height=\"$2\" width=\"$3\"/>"),
            ("apex:form\tVF", "apex:form id=\"$1\">\n\t$2\n</apex:form>"),
            ("apex:iframe\tVF", "apex:iframe src=\"$1\" scrolling=\"$2\" id=\"$3\"/>"),
            ("apex:image\tVF", "apex:image id=\"$1\" value=\"$2\" width=\"$3\" height=\"$4\"/>"),
            ("apex:include\tVF", "apex:include pageName=\"$1\"/>"),
            ("apex:includeScript\tVF", "apex:includeScript value=\"$1\"/>"),
            ("apex:inlineEditSupport\tVF", "apex:inlineEditSupport showOnEdit=\"$1\" cancelButton=\"$2\" hideOnEdit=\"$3\" event=\"$4\"/>"),
            ("apex:inputCheckbox\tVF", "apex:inputCheckbox value=\"$1\"/>"),
            ("apex:inputField\tVF", "apex:inputField value=\"$1\"/>"),
            ("apex:inputHidden\tVF", "apex:inputHidden value=\"$1\"/>"),
            ("apex:inputSecret\tVF", "apex:inputSecret value=\"$1\"/>"),
            ("apex:inputText\tVF", "apex:inputText value=\"$1\"/>"),
            ("apex:inputTextarea\tVF", "apex:inputTextarea value=\"$1\"/>"),
            ("apex:insert\tVF", "apex:insert name=\"$1\"/>"),
            ("apex:listViews\tVF", "apex:listViews name=\"$1\"/>"),
            ("apex:message\tVF", "apex:message for=\"$1\"/>"),
            ("apex:messages\tVF", "apex:messages />"),
            ("apex:outputField\tVF", "apex:outputField value=\"$1\"/>"),
            ("apex:outputLabel\tVF", "apex:outputLabel value=\"$1\" for=\"$2\"/>"),
            ("apex:outputLink\tVF", "apex:outputLink value=\"$1\"/>"),
            ("apex:outputPanel\tVF", "apex:outputPanel id=\"$1\">\n\t$2\n</apex:outputPanel>"),
            ("apex:outputText\tVF", "apex:outputText value=\"$1\"/>"),
            ("apex:page\tVF", "apex:page id=\"$1\">\n\t$2\n</apex:page>"),
            ("apex:pageBlock\tVF", "apex:pageBlock mode=\"${1:detail}\">\n\t$2\n</apex:pageBlock>"),
            ("apex:pageBlockButtons\tVF", "apex:pageBlockButtons>\n\t$1\n</apex:pageBlockButtons>"),
            ("apex:pageBlockSection\tVF", "apex:pageBlockSection title=\"$1\" columns=\"$2\">\n\t$3\n</apex:pageBlockSection>"),
            ("apex:pageBlockSectionItem\tVF", "apex:pageBlockSectionItem>\n\t$1\n</apex:pageBlockSectionItem>"),
            ("apex:pageBlockTable\tVF", "apex:pageBlockTable value=\"$1\" var=\"$2\">\n\t$3\n</apex:pageBlockTable>"),
            ("apex:pageMessage\tVF", "apex:pageMessage summary=\"$1\" serverity=\"$2\" strength=\"${3:3}\"/>"),
            ("apex:pageMessages\tVF", "apex:pageMessages />"),
            ("apex:panelBar\tVF", "apex:panelBar>\n\t$1\n</apex:panelBar>"),
            ("apex:panelBarItem\tVF", "apex:panelBarItem label=\"$1\">$2<apex:panelBarItem/>"),
            ("apex:panelGrid\tVF", "apex:panelGrid columns=\"$1\">\n\t$2\n</apex:panelGrid>"),
            ("apex:panelGroup\tVF", "apex:panelGroup id=\"$1\">\n\t$2\n</apex:panelGroup>"),
            ("apex:param\tVF", "apex:param value=\"$1\"/>"),
            ("apex:relatedList\tVF", "apex:relatedList list=\"$1\"/>"),
            ("apex:repeat\tVF", "apex:repeat value=\"$1\" var=\"$2\">\n\t$3\n</apex:repeat>"),
            ("apex:selectCheckboxes\tVF", "apex:selectCheckboxes value=\"$1\">\n\t$2\n</apex:selectCheckboxes>"),
            ("apex:selectList\tVF", "apex:selectList value=\"$1\" size=\"$2\">\n\t$3\n</apex:selectList>"),
            ("apex:selectOption\tVF", "apex:selectOption itemValue=\"$1\" itemLabel=\"$2\"/>"),
            ("apex:selectOptions\tVF", "apex:selectOptions value=\"$1\"/>"),
            ("apex:selectRadio\tVF", "apex:selectRadio value=\"$1\">\n\t$2\n</apex:selectRadio>"),
            ("apex:stylesheet\tVF", "apex:stylesheet value=\"$1\"/>"),
            ("apex:tab\tVF", "apex:tab label=\"$1\" name=\"$2\"/>"),
            ("apex:tabPanel\tVF", "apex:tabPanel>\n\t$2\n</apex:tabPanel>"),
            ("apex:toolbarGroup\tVF", "apex:toolbarGroup itemSeparator=\"$1\" id=\"$2\">\n\t$3\n</apex:toolbarGroup>"),
            ("apex:variable\tVF", "apex:variable var=\"$1\" value=\"$2\"/>"),
            ("apex:vote\tVF", "apex:vote objectId=\"$1\"/>")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
